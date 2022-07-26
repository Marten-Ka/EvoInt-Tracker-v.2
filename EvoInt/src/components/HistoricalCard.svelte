<script lang="ts">
	export let img_link: string;
	export let img_alt: string;
	export let source_link: string;
	export let source_text: string;
	export let heading: string;
	export let content: string;
	export let tag_list: string[];
	export let button_link: string;
</script>

<div class="md:flex flex-start">
	<div class="bg-blue-600 w-6 h-6 flex items-center justify-center rounded-full -ml-3">
		<svg
			aria-hidden="true"
			focusable="false"
			data-prefix="fas"
			class="text-white w-3 h-3"
			role="img"
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 448 512"
		>
			<path
				fill="currentColor"
				d="M0 464c0 26.5 21.5 48 48 48h352c26.5 0 48-21.5 48-48V192H0v272zm64-192c0-8.8 7.2-16 16-16h288c8.8 0 16 7.2 16 16v64c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16v-64zM400 64h-48V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H160V16c0-8.8-7.2-16-16-16h-32c-8.8 0-16 7.2-16 16v48H48C21.5 64 0 85.5 0 112v48h448v-48c0-26.5-21.5-48-48-48z"
			/>
		</svg>
	</div>
	<div class="max-w-md rounded overflow-hidden shadow-lg ml-6 mb-6">
		<div class="relative group">
			<img class="w-full block h-auto" src={img_link} alt={img_alt} />
			<a
				href={source_link}
				target="_blank"
				class="source opacity-0 bottom-0 absolute text-left group-hover:opacity-80 w-full border-[0.5px] rounded-t bg-gray-200 text-gray-700 px-6 py-1"
			>
				{source_text}
			</a>
		</div>
		<div class="px-6 py-4 bg-gray-100">
			<div class="font-bold text-2xl mb-2">{heading}</div>
			<p class="text-gray-700 text-lg">
				{content}
			</p>
		</div>
		<div class="flex flex-col gap-4 px-6 pt-4 pb-4 bg-gray-100">
			<div>
				{#each tag_list as tag}
					<span
						class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
					>
						{tag}
					</span>
				{/each}
			</div>
			<div>
				<form action={button_link}>
					<button
						type="submit"
						class="inline-block px-4 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out"
						data-mdb-ripple="true"
					>
						Read more
					</button>
				</form>
			</div>
		</div>
	</div>
</div>

<style lang="postcss">
	@media only screen and (hover: none) and (pointer: coarse) {
		.source {
			opacity: 80;
		}
	}
</style>
